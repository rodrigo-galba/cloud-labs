package main

import (
	"database/sql"
	"fmt"
	"github.com/gin-gonic/gin"
	"github.com/go-sql-driver/mysql"
	"net/http"
	"os"
	"rsc.io/quote"
	"strconv"

	_ "github.com/go-sql-driver/mysql"
)

type Album struct {
	ID     int  `json:"id"`
	Title  string  `json:"title"`
	Artist string  `json:"artist"`
	Price  float64 `json:"price"`
}

func main() {
	router := gin.Default()
	router.GET("/", index)
	router.GET("/albums", getAlbums)
	router.GET("/albums/:id", getAlbumByID)
	router.POST("/albums", postAlbums)

	router.Run("localhost:5000")
}

func index(c *gin.Context) {
	c.IndentedJSON(http.StatusOK, gin.H{
		"message": quote.Hello(),
		"APP_NAME": os.Getenv("APP_NAME"),
		"status": http.StatusOK})
}

func dbConn() (db *sql.DB) {
	// Capture connection properties.
	cfg := mysql.Config{
		User:   os.Getenv("db_user"),
		Passwd: os.Getenv("db_pass"),
		Net:    "tcp",
		Addr:   os.Getenv("db_url"),
		DBName: os.Getenv("db_name"),
	}
	// Get a database handle.
	var err error
	db, err = sql.Open("mysql", cfg.FormatDSN())
	if err != nil {
		panic(err.Error())
	}
	return db
}

// getAlbums responds with the list of all albums as JSON.
func getAlbums(c *gin.Context) {
	db := dbConn()
	selDB, err := db.Query("SELECT * FROM album ORDER BY id DESC")
	if err != nil {
		panic(err.Error())
	}

	item := Album{}
	albums := []Album{}

	for selDB.Next() {
		err = selDB.Scan(&item.ID, &item.Title, &item.Artist, &item.Price)
		if err != nil {
			panic(err.Error())
		}
		albums = append(albums, item)
	}
	defer db.Close()

	c.IndentedJSON(http.StatusOK, albums)
}

// postAlbums adds an Album from JSON received in the request body.
func postAlbums(c *gin.Context) {
	var newAlbum Album

	// Call BindJSON to bind the received JSON to
	// newAlbum.
	if err := c.BindJSON(&newAlbum); err != nil {
		return
	}

	// Add the new Album to the slice.
	//albums = append(albums, newAlbum)
	c.IndentedJSON(http.StatusCreated, newAlbum)
}

// getAlbumByID locates the Album whose ID value matches the id
// parameter sent by the client, then returns that Album as a response.
func getAlbumByID(c *gin.Context) {
	input := c.Param("id")
	id, _ := strconv.Atoi(input)
	albums, err := albumsById(id)
	if err != nil {
		c.IndentedJSON(http.StatusNotFound, gin.H{"message": "Album not found"})
	} else {
		c.IndentedJSON(http.StatusOK, albums)
	}
}

// albumsByArtist queries for albums that have the specified artist name.
func albumsById(id int) ([]Album, error) {
	var albums []Album

	db := dbConn()
	rows, err := db.Query("SELECT * FROM album WHERE id = ?", id)
	if err != nil {
		return nil, fmt.Errorf("albumsById %q: %v", id, err)
	}
	defer rows.Close()
	// Loop through rows, using Scan to assign column data to struct fields.
	for rows.Next() {
		var alb Album
		if err := rows.Scan(&alb.ID, &alb.Title, &alb.Artist, &alb.Price); err != nil {
			return nil, fmt.Errorf("albumsById %q: %v", id, err)
		}
		albums = append(albums, alb)
	}
	if err := rows.Err(); err != nil {
		return nil, fmt.Errorf("albumsById %q: %v", id, err)
	}
	return albums, nil
}

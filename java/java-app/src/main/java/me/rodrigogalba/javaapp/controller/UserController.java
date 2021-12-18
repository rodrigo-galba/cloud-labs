package me.rodrigogalba.javaapp.controller;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import me.rodrigogalba.javaapp.model.User;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.ArrayList;
import java.util.List;

@RestController
@RequestMapping("/users")
@RequiredArgsConstructor
@Slf4j
public class UserController {

    @GetMapping("/")
    public List<User> index() {
        log.info("listing users");
        List<User> users = new ArrayList<User>();
        users.add(User.builder().name("John Doe").login("johndoe").build());
        users.add(User.builder().name("Janedoe").login("janedoe").build());
        users.add(User.builder().name("Me").login("mee").build());
        return (List<User>) users;
    }

}

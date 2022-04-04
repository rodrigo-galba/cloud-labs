# HTTP(S) benchmark tools, testing/debugging, & restAPI (RESTful)

## ALI

> ali – Generate HTTP load and plot the results in real-time, written in Go (golang)

[Doc](https://github.com/nakabonne/ali)

### Installation

```
wget https://github.com/nakabonne/ali/releases/download/v0.7.3/ali_0.7.3_linux_amd64.deb
apt install ./ali_0.7.3_linux_amd64.deb
```

### Usage

```
ali http://host.xz
```
> Replace `http://host.xz` with the target you want to issue the requests to. Press Enter when the UI appears, then the attack will be launched with default options (rate=50, duration=10s).

-------------------------------------------------------------------------------------

References

[http awesome](https://github.com/denji/awesome-http-benchmark)
# Rust Language

## Installation

### Windows

- Download Microsoft C++ build tools.  
- Download rustup tool

### Linux

- Install `build essential` package.
```
sudo apt install build-essential
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source "$HOME/.cargo/env"
```

## Update

If you've installed rustup in the past, you can update your installation by running rustup update. 

## Uninstall

If at any point you would like to uninstall Rust, you can run rustup self uninstall. We'll miss you though! 

## Configuring the PATH environment variable

In the Rust development environment, all tools are installed to the `~/.cargo/bin` directory, and this is where you will find the Rust toolchain, including rustc, cargo, and rustup.

Accordingly, it is customary for Rust developers to include this directory in their PATH environment variable. During installation rustup will attempt to configure the PATH. Because of differences between platforms, command shells, and bugs in rustup, the modifications to PATH may not take effect until the console is restarted, or the user is logged out, or it may not succeed at all.

If, after installation, running `rustc --version` in the console fails, this is the most likely reason. 

-------------------------

References

- https://visualstudio.microsoft.com/pt-br/visual-cpp-build-tools/
- https://learn.microsoft.com/en-us/windows/dev-environment/rust/setup
- https://www.rust-lang.org/tools/install

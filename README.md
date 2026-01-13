# acmsg (automated commit message generator)

A cli tool written in Python that generates git commit messages using AI models
through the OpenRouter API.

[![Create Release and Publish to PyPI](https://github.com/quinneden/acmsg/actions/workflows/publish-and-release.yaml/badge.svg)](https://github.com/quinneden/acmsg/actions/workflows/publish-and-release.yaml)
[![Run Tests](https://github.com/quinneden/acmsg/actions/workflows/test.yaml/badge.svg?branch=main)](https://github.com/quinneden/acmsg/actions/workflows/test.yaml)

## Features

- Analyzes staged changes in your git repository
- Generates contextual commit messages using AI
- Supports multiple AI models via [OpenRouter](https://openrouter.ai)
- Configurable AI model and temperature settings
- Optional emoji prefixes in commit messages
- Optionally edit generated commit message
- Automatically commits changes with generated message, if confirmed

## Prerequisites
- OpenRouter API Key

## Installation

### with pipx:
```bash
pipx install acmsg
```

### with nix:
using flakes (i.e. nixos/nix-darwin/home-manager):
```bash
# Add `acmsg` to your flake inputs
inputs.acmsg.url = "github:quinneden/acmsg";

# Add the nixpkgs overlay & include the package in your configuration
nixpkgs.overlays = [ inputs.acmsg.overlays.default ];
environment.systemPackages = [ pkgs.acmsg ];
# or home.packages = [ pkgs.acmsg ];

# Or include the package directly from inputs
environment.systemPackages = [ inputs.acmsg.packages.${pkgs.system}.acmsg ];
```
using a standalone profile:
```bash
$ nix profile install "github:quinneden/acmsg"
```

## Configuration

The configuration file is located at `~/.config/acmsg/config.yaml`.

On first run, acmsg will prompt you to configure your OpenRouter API token.

You can also run the following command:
```bash
$ acmsg config set api_token <your_api_token>
```

## Usage

### Commit

```bash
acmsg commit
```

Generate a commit message for staged changes.

Options:
- `--model MODEL`: Specify the AI model (overrides config)
- `--temperature TEMP`: Set model temperature (0.0-2.0, overrides config)
- `--use-emojis`: Enable emoji prefixes in commit messages
- `--no-use-emojis`: Disable emoji prefixes in commit messages

### Config

```bash
acmsg config set <parameter> <value>
acmsg config get <parameter>
```

Manage configuration settings.

Available parameters:
- `api_token`: OpenRouter API key
- `model`: AI model to use (default: qwen/qwen3-30b-a3b:free)
- `temperature`: Model temperature (0.0-2.0, default: 0.8)
- `use_emojis`: Enable emoji prefixes (true/false, default: false)

## License

acmsg is licenced under the MIT License, as included in the [LICENSE](LICENSE) file.

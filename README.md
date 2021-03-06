# Sublime Contrib Golinters

`sublimelinter-contrib-golinters` provides an interface to both `golint`, and `gometalint` that is compatible with SublimeLinter. Unlike other linters, this one does not prefer one, or the other, and is compatible with both of the linters, all you need to do is adjust the command, and win.

## Help
### `go mod` (`GO111MODULE`)?

If you are using `go mod` you will need to create a wrapper, because of the way that SublimeLinter works.  It would seem that the `env` option doesn't work that well from settings, and we are unable to easily set the env.  Your wrapper should just wrap like below (typically I put this file in `~/.bin/subl-golint`)

```bash
#!/bin/bash
export GO111MODULE=auto
"$@"
```

Then in your settings do

```json
{
  "linters": {
    "golint": {
      "executable": "/Users/user/.bin/subl-golint",
      "args": [
        "gometalinter",

        "--fast",
        "--vendor",
        "--disable-all",
        "--tests",

        "--enable=gosec",
        "--enable=golint",
        "--enable=errcheck",
        "--enable=ineffassign",
        "--enable=vetshadow",
        "--enable=goconst",
        "--enable=gocyclo",
        "--enable=deadcode",
        "--enable=safesql",
        "--enable=vet"
      ]
    }
  }
}
```

***Notice how "gometalinter" is the first argument.  This should always be the case when replacing the exectuable, (in that it should be `golint`, or `gometalinter` so that we can send `--include` with the path of the file, or append the file. We will also remove that argument so that you don't have to account for it in your wrapper... or executable.****

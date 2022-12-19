{
    "targets": [{
        "target_name": "gpac",
        "sources": [ "./src/gpac_napi.c"],
        "include_dirs": [ "<!@(brew --prefix)/include" ],
        "libraries": [ "-lgpac"],
    }]
}


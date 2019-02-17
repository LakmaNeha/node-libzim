{
	"variables": {
      "libzim_dir": "<(module_root_dir)/../../download",
	  "libzim_include": "../../download/include",
  	},
	"targets": [
		{
			"conditions": [
				["OS=='linux'", {
					"libraries": [ 
						"-Wl,-rpath,<(libzim_dir)",
						"-L<(libzim_dir)",
						"<(libzim_dir)/libzim.so.4",
					],
				}],
				["OS=='mac'", {
					"libraries": [ "-lzim" ]
				}],
			],
			"include_dirs": [
				"<(libzim_include)",
			],
			"includes": [
				"../auto.gypi",
				"../../sources.gypi"
			],
		}
	],
	"includes": [
		"../auto-top.gypi"
	]
}
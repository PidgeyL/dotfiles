--
-- This plugin adds a custom colorscheme.
--

VERSION = "1.0.0"

local config = import("micro/config")

config.AddRuntimeFile("pidgey", config.RTColorscheme, "pidgey.micro")

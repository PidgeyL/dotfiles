--
-- This plugin adds a custom colorscheme.
--

VERSION = "1.0.0"

local config = import("micro/config")
local shell  = import("micro/shell")

config.AddRuntimeFile("pidgey", config.RTColorscheme, "pidgey.micro")

function init()
	config.MakeCommand("run_code", run_code, config.NoComplete)
end

function run_code(bp)
    local buf = bp.Buf
        -- the true means run in the foreground
        -- the false means send output to stdout (instead of returning it)
    if buf:FileType() == "go" then
        shell.RunInteractiveShell("go run " .. buf.Path, true, false)
    elseif buf:FileType() == "python" then
        shell.RunInteractiveShell("python " .. buf.Path, true, false)
    end
end

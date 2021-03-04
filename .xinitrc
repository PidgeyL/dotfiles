# Load colour scheme if available
if [ -f ~/.Xresources ]; then
     xrdb -merge .Xresources
fi

# Start graphical environment
if [ "$X_ENV" = i3 ]; then
    exec i3
fi


if [ "$X_ENV" = qtile ]; then
    exec qtile start
fi


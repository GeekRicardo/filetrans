time=$(date "+%y.%m.%d")
if [ ! -f "log/$time.log" ]; then
	mv log.log log/$time.log
else
	cat log.log >> log/$time.log
fi
sudo python3 main.py >  log.log 2>&1 &

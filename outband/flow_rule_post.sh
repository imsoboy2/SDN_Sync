CONTROLLER_IP= Your controller IP address
CONTROLLER_PORT= Your controller port number


StartTime=$(date +%s.%N)
for i in `seq 1 5000`
do
  curl -X POST --header "Content-Type: application/json" --header "Accept: application/json" -d @${1}${i}.json "ADDRESS FOR CONTROLLER SHARD" --user karaf:karaf

  
done
EndTime=$(date +%s.%N)
result=$( echo "scale=4; ${EndTime}-${StartTime}" |bc )
echo "result = ${result}"

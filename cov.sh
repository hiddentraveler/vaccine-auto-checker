timeout 10s rm -rf test.json check.json && python3 covidbypincode.py | jq > test.json && cat test.json| grep available_capacity > check.json 
if diff -q default.json check.json | grep -q 'Files default.json and check.json differ'; then
  python3 telegram.py
fi
cat check.json > default.json
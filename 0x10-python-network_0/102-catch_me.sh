#!/bin/bash
# Request that makes 0.0.0.0:5000/catch_me to respond with You got me!
curl -sL -X PUT -H "Origin: HoberltonSchool" -d "user_id=98" 0.0.0.0:5000/catch_me

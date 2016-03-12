# github-internet-button

Github integration with the particle internet button via AWS. Flash an LED on the internet button when someone pushes to a repository

## Setup:

- Create an AWS python-based lambda function with the contents of call_particle.py
- Create an AWS Api Gateway POST resource with an Integration Request mapping template:

```
{
    "particle_access_token" : "your_token",
    "particle_device_id" : "your_device_id",
    "body" : $input.json('$')
}
```

  (You can just bake this into the python script but I don't want to commit my credentials :) )
  
- Hook up the POST resource to the lambda
- Add a webhook to the git repositories to POST to the resource
- Connect your internet button
- Be amazed

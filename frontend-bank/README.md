# Bank Frontend

### Launch

to launch the bank frontend, go to the projects root directory and run 

```bash
python3 frontend-bank/main.py
```

after having installed all dependencies using

```bash
pip3 install -r frontend-bank/requirements.txt
```

### Pages

The frontend has a login and a register page which have to be used to create a session token in the background. 

Afterwards the following sites can be accessed:

path | description
-----|------------
/    | home
/login | login using existing email and password
/sign-up | sign up using wallet address
/logout | log out
/fund | mint new USD stablecoins to own address
/refund | if user not bank, show burn address <br/>
 | if user is bank, give opportunity to burn directly


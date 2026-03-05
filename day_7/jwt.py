# jwt 

"""
jwt stands for json web tocken it is a way to handle authentication or autherization betweeen the cliemt and server .
    without server  side session create kare ...

jwt is also use in stateless authentication system

jwt structurized in three parts :-

        header :
                {
        "alg": "HS256",
        "typ": "JWT"
        }



        payload:
                {
        "user_id": 101,
        "role": "admin",
        "exp": 1700000000
        }
    
        signature :
        generate through the secret key 

        HMACSHA256(
        base64UrlEncode(header) + "." +
        base64UrlEncode(payload),
        secret
        )

        
how jwt authenctication workflow happens:
    firstly user login through username and passward

    server verrify their credentials 
    
    and then server will generate the tokens for users 
    
    client stores that tokens in like localhost or httponly
    
    in each request the usr will send the tokens to prove their identity 
    
    server verify the each tokens eveery time 
    
    if the tokens are valid then :
        request allow 
    else :
        invalid or expired / 401 unathorized....


? jwt two important concept :
        Access tockens 
            short expiry (15 min to 1 hour)
            api related access
        
        refersh tokens 
            long expiry
            used to generate new access tokens 


from jose import jwt

SECRET_KEY = "mysecret"
ALGORITHM = "HS256"

def create_token(data: dict):
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

def verify_token(token: str):
    return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
























"""
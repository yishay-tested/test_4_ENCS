from fastapi import FastAPI, HTTPException
import uvicorn
import requests
from pydantic import BaseModel

import json

app = FastAPI()

class CipherRequest(BaseModel):
    text: str
    offset: int
    mode: str # Expects "encrypt" or "decrypt"

def caesar(text:str,offset:int=1,mode:str|str="encrypt"):
    pass


@app.post("/caesar")
def caesar_POST(data: CipherRequest|dict): # mode:"encrypt"|”decrypt”
    '''Caesar cipher endpoint: POST /caesar Body:{ "text": string, "offset": int, "mode": "encrypt"/”decrypt” } 
    Response: { "encrypted_text": "..." } or: { "decrypted_text": "..." } 
    Description: Encrypts or decrypts text using a Caesar cipher with a specified offset. 
    '''
    if type(data) == type({}):
        print(data['text'],"being",data['mode'],"by offset of",data['offset'])
        return  { "encrypted_text": "..." }


    text = data.text
    offset = data.offset
    mode = data.mode
    print(text,"being",offset,"by offset of",mode)
    
    # with open("file.json",'r') as f:
    #     body_json_dict = json.load(f)
    #     print(body_json_dict['text'],"being",body_json_dict['mode'],"by offset of",body_json_dict['offset'])

    response = caesar(text,offset,mode)

    if mode == "encrypt":
        return { "encrypted_text": "..." }
    elif mode == "decrypt":
        return { "decrypted_text": "..." }

'''Caesar cipher endpoint: POST /caesar Body:{ "text": string, "offset": int, "mode": "encrypt"/”decrypt” } 
Response: { "encrypted_text": "..." } or: { "decrypted_text": "..." } 
Description: Encrypts or decrypts text using a Caesar cipher with a specified offset. 
'''

'''
Fence cipher endpoints: GET /fence/encrypt?text=<text> 
Response: { "encrypted_text": "..." } 
Description - Extracts the text from the URL and encrypts it using the fence cipher 
'''

'''
POST /fence/decrypt Body: { "text": "string" } 
Response: { "decrypted": "..." } 
Description - Gets the text from the request body and decrypts it using the fence cipher.
'''



@app.get("/hello")
def read_root():
    return {"message": "Hello World"}

@app.get("/hello2")
def read_root():
    return {"message": "Hello World2"}



if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)

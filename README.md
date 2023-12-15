# STK

### Installation

1. Pull down repo.
2. Create an `.env` file and copy in the values provided.
3. Run `docker-compose build` to build the app containers.
4. Run `docker-compose up` to run.

### Running

- App is available at `localhost`.
- Backend service (dic-fulfillment) runs on `http://localhost:5000`.
- Frontend service (frontend) runs on `http://localhost:3000`.

Once all services are up, we should see 

```
[+] Running 6/6
 ⠿ Network stk_default        Created
 ⠿ Volume "stk_styktin"       Created
 ⠿ Container frontend         Started
 ⠿ Container dic-fulfillment  Started
 ⠿ Container mongo            Started
 ⠿ Container nginx            Started
 ```
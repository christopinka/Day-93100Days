# API? Spotify? Verify!

The APIs we've been using so far are pretty unusual in that they provide their service for free.

Normally, you have to pay to use an APIs data services (at least if you're doing so commercially). This means that you will need to verify your status as an approved user before you can get your grubby hands on all of that sweet, sweet data!

Today, we're learning how to write a program that tells an API that we've got an account before accessing its info.

Don't worry, you won't have to bust out the credit card. We're using a Spotify API that won't charge provided we keep our usage under a certain level.

*Note:* Spotify has reserved this API for production level apps. To ensure that we can continue using the API to learn and build in 100DoC, we ask that you please refrain from requesting quota extensions from Spotify for your 100DoC projects.

## Get started 
👉  [Click here to go to the Spotify developer page](https://developer.spotify.com/dashboard/) and log in/create an account.

👉 Next, hit *create app* and give it a name and description.

![](resources/01_api1.png)

👉 Copy the **client ID** and **insert it as a secret in your REPL**.  Make sure to call it **CLIENT_ID**.
![](resources/01_api2.png)

![](resources/01_api3.png)

## Client Secret
👉 Back to Spotify and click **show client secret** (use your own, not the one in these screenshots, I'll have changed it by the time this goes out).
![](resources/01_api4.png)
Again, copy and create a REPL secret for it - **CLIENT_SECRET**.
![](resources/01_api5.png)

Now we have, effectively, the username and password that our program needs so that it can talk to Spotify.
# Generate Receipt

`generate_receipt.exe` is a Python-based utility that generates a receipt image for Twitch streamers when a user follows or subscribes to their channel. The generated receipt includes the user's name, action (followed or subscribed), subscription tier, duration, and a QR code linking to the follower's Twitch profile.


<p align="center">
  <img src="https://cdn.discordapp.com/attachments/1232761498170953749/1279157338732888187/follow_receipt.png?ex=66d36b9b&is=66d21a1b&hm=0bf986f8a7ff3feef286580e92b2d2994fdad65993180335b0ba881a02bc26f3&" alt="Receipt Example">
</p>


## Features

- Generates a realistic-looking receipt with details about the follow or subscription.
- Supports different subscription tiers (Tier 1, Tier 2, Tier 3, Prime).
- Includes a customizable thank-you message.
- Automatically generates a QR code linking to the follower's Twitch profile.
- Adds a random "cash" value and calculates the change, mimicking a real cash receipt.

## Usage

To use the `generate_receipt.exe`, simply download the latest release from the [Releases](https://github.com/StressDemon/receipt-maker/releases) page. Run the exe from the command line with the following options:

```
generate_receipt.exe <streamer_name> <follower_name> <action> [options]
```

### Arguments

- `streamer_name`: The name of the streamer.
- `follower_name`: The name of the follower or subscriber.
- `action`: Either `followed` or `subscribed`.

### Optional Parameters

- `--tier`: Subscription tier (1, 2, 3, or prime). Defaults to `1`.
- `--months`: Number of months for a subscription. Defaults to `1`.
- `--address`: Streamer's supermarket address. Defaults to `"1234 Streamer Lane, Twitch City"`.
- `--thank_you`: Custom thank you message from the streamer. Defaults to `"THANK YOU!"`.
- `--sub_message`: Custom message from the subscriber to display under the QR code. Defaults to `None`.

## Example for a tier 2 sub for 3 months

```
generate_receipt.exe "StreamerName" "FollowerName" "subscribed" --tier 2 --months 3 --thank_you "Much appreciated!" --sub_message "I was chased by a pitbul as a child!"
```
```
generate_receipt.exe "StreamerName" "Follower123" "followed" --thank_you "Welcome to the stream!"
```
```
generate_receipt.exe "StreamerName" "PrimeUser" "subscribed" --tier prime --address "5678 Prime Lane, Twitchville" --thank_you "Thank you for using Prime!" --sub_message "Ducks make me confused about my sexuality!"
```

## Download

You can download the latest version of the executable from the [Releases](https://github.com/StressDemon/reciept-maker/releases) page.

new_line = '\n'


def event_message(event_details, user_last_activity_date, user_signup_date):
    return {
        "attachments": [{
            "fallback":
            f"Message for {event_details['username']} errored",
            "color":
            "#396",
            "blocks": [{
                "type": "section",
                "text": {
                    "type":
                    "mrkdwn",
                    "text":
                    f"<https://github.com/{event_details['username']}|{event_details['username']}> performed *{len(event_details['events'])}* events today.\n\n*Last Activity*\n {user_last_activity_date}\n\n*Signed Up*\n {user_signup_date}"
                },
                "accessory": {
                    "type":
                    "overflow",
                    "options": [{
                        "text": {
                            "type": "plain_text",
                            "text": "GitHub Profile"
                        },
                        "url":
                        f"https://github.com/{event_details['username']}"
                    }]
                }
            }, {
                "type": "section",
                "text": {
                    "type":
                    "mrkdwn",
                    "text":
                    f"*Events Today*\n{''.join([f'{new_line}•{x}' for x in (event_details['events'])[:event_details['parent_event_count']]])}"
                }
            }, {
                "type":
                "context",
                "elements": [{
                    "type": "image",
                    "image_url":
                    f"https://github.com/{event_details['username']}.png",
                    "alt_text": f"{event_details['username']} avatar"
                }]
            }]
        }]
    }

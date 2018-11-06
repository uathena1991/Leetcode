# The people who buy ads on our network don't have enough data about how ads are working for their business. They've asked us to find out which ads produce the most purchases on their website.

# Our client provided us with a list of user IDs of customers who bought something on a landing page after clicking one of their ads:

# Each user completed 1 purchase.
completed_purchase_user_ids = [
    "3123122444","234111110", "8321125440", "99911063"]

# And our ops team provided us with some raw log data from our ad server showing every time a user clicked on one of our ads:

ad_clicks = [
    "IP_Address,Time,Ad_Text",
    "122.121.0.1,2016-11-03 11:41:19,Buy wool coats for your pets",
    "96.3.199.11,2016-10-15 20:18:31,2017 Pet Mittens",
    "122.121.0.250,2016-11-01 06:13:13,The Best Hollywood Coats",
    "82.1.106.8,2016-11-12 23:05:14,Buy wool coats for your pets",
    "92.130.6.144,2017-01-01 03:18:55,Buy wool coats for your pets",
    "92.130.6.145,2017-01-01 03:18:55,2017 Pet Mittens",
]

# The client also sent over the IP addresses of all their users.

all_user_ips = [
    "User_ID,IP_Address",
     "2339985511,122.121.0.155",
    "234111110,122.121.0.1",
    "3123122444,92.130.6.145",
    "39471289472,2001:0db8:ac10:fe01:0000:0000:0000:0000",
    "8321125440,82.1.106.8",
    "99911063,92.130.6.144"
]

# Write a function to parse this data, determine how many times each ad was clicked, then return how many of those ad clicks were from users who made a purchase.

# Expected output:

# 1 of 2    2017 Pet Mittens
# 0 of 1    The Best Hollywood Coats
# 3 of 3    Buy wool coats for your pets





# IP_dict['IP'] = User_id
# ad_dict['ad'] = [IP_dict[ip_x], ...] # click on that
# res_dict['ad'] = (num_click, num_purchase) #  (0, 0)
# for ad in ad_dict:
#     res_dict['ad'][0] = len(ad_dict[ad])
#     for users in ad_dict[ad]:
#         if users in completed_purchase_user_ids:
#              res_dict['ad'][1] += 1
# return res_dict



def common_longest_sequences(user0, user1):
    max_len, max_idx = 0, 0
    dp_list = [[0 for _ in range(len(user1)+1)] for _ in range(len(user0)+1)]
    for i in range(len(user0)):
        for j in range(len(user1)):
            if user0[i] == user1[j]:
                dp_list[i+1][j+1] = dp_list[i][j] + 1
            if max_len < dp_list[i+1][j+1]:
                max_len = dp_list[i+1][j+1]
                max_idx = i+1
    for x in dp_list:
        print(x)

    res_sequence = user0[max_idx-max_len:max_idx]

    return res_sequence


# print(common_longest_sequences(user0, user2))
# print(common_longest_sequences(user0, user1))
# print(common_longest_sequences(user0, user3))
# print(common_longest_sequences(user3, user1))
# print(common_longest_sequences(user2, user1))
# print(common_longest_sequences(user2, user3))

# from collections import defaultdict
# def click_counts(inputs):
#     res_dict = defaultdict(int)
#     for r in counts:
#         click, domain = r.split(',')
#         click = int(click)
#         subdoms = domain.split('.')
#         for i in range(len(subdoms)):
#             curr_sd = '.'.join(subdoms[i:])
#             res_dict[curr_sd] += click
#     return res_dict

# print(click_counts(counts))
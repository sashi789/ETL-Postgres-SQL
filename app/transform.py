import pandas as pd

def join_users_posts(users, posts):
    df_users = pd.DataFrame(users)
    df_posts = pd.DataFrame(posts)

    merged_df = df_posts.merge(df_users, left_on='userId', right_on='id', how='inner')
    final_df = merged_df[["id_x", "title", "body", "name", "email"]].copy()
    final_df.rename(columns={
        "id_x": "PostId",
        "title": "PostTitle",
        "body": "PostBody",
        "name": "UserName",
        "email": "UserEmail"
    }, inplace=True)
    return final_df

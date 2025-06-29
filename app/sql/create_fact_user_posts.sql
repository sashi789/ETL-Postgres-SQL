IF NOT EXISTS (SELECT * FROM sysobjects WHERE name='FactUserPosts' AND xtype='U')
CREATE TABLE FactUserPosts (
    PostId INT PRIMARY KEY,
    PostTitle NVARCHAR(MAX),
    PostBody NVARCHAR(MAX),
    UserName NVARCHAR(255),
    UserEmail NVARCHAR(255)
);

USE [HMS]
GO

/****** Object:  Table [dbo].[CustomerInfo]    Script Date: 1/15/2021 6:45:11 PM ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[CustomerInfo](
	[CustomerID] [int] NULL,
	[CustomerName] [nvarchar](50) NULL,
	[PhoneNo] [nvarchar](50) NULL,
	[Address] [nvarchar](max) NULL,
	[CheckinDate] [datetime] NULL,
	[CheckoutDate] [datetime] NULL,
	[RoomType] [nvarchar](200) NULL,
	[Price] [int] NULL,
	[NoofDays] [int] NULL,
	[RestaurentCharges] [int] NULL,
	[TotalAmount] [int] NULL,
	[CreatedDate] [datetime] NULL
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO




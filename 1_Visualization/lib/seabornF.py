from re import X
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud, STOPWORDS


Noi_dung = """
    1. Seaborn: được xây dựng trên thư viện trực quan cốt lõi của python là matplotlib => Là bổ sung không phải thay thế cho matplotlib
    2. Tính năng
        - Trực quan dữ liệu 2 biến và 3 biến
        - Phù hợp và hình dung các mô hình hồi quy tuyến tính
        - Lập kế hoạch dữ liệu chuỗi thời gian thống kê
        - Seaborn hoạt động tốt với cấu trúc dữ liệu Numpy và pandas
        - Nó đi kèm với các theme để tạo kiểu dữ liệu matplotlib đồ họa
    3. Điểm hơn seaborn so với malplotlib
        - Các tham số malplotlib mặc định => Seaborn  hoạt hộng với các tham số tùy chỉnh khác nhau
        - Malplotlib làm việc với Dataframe không suôn sẻ => Chỉ làm việc với các cột dữ liệu cụ thể trên Dataframe
    4. Vẽ biểu đồ trong seaborn
        - sb.distplot(): vẽ 1 phần bố quan sát đơn biến => Tương tự như histogram => Sử dụng để mực độ lệch chuẩn
        - Distribution plot: thay thể để hiển thị sự phân phối của dữ liệu/ một kde curve và một rug plot có thể kết hợp với nhau
        - Regression plot: scatter plot với một regression line/ cách sử dụng tương tự như distplot/ Các biến dữ liệu và x và y phải được xác định
        - Scatter plot: phân loại với các điểm không chồng chéo
        - Boxplot: vẽ plot để hiển thị các phân phối liên quan đến category
        - Barplot: vẽ plot để hiển thị dữ liệu dưới dạng khối hình chữ nhật
        - Lineplot: vẽ plot để hiển thị dữ liệu dưới dạng line
"""


# Viết hàm

# Load file dữ liệu
def load_data(file_path):
    df = pd.read_csv(file_path)
    return df



# Biểu đồ countPlot: hiển biểu đồ thống kê dữ liệu theo static
# Mục đích: Dùng để phân loại và theo categorical
def count_plot(x, y, data, title, Width=8, Height=6, fontsize=12, rotation=60):
    plt.figure(figsize=(Width, Height)) # Kích thước của dữ liệu
    plt.title(title) # Title của dữ liệu
    plt.xticks(rotation=rotation, fontsize=fontsize) # Chỉnh bên trong dữ liệu
    sns.countplot(x=x, hue=y , data=data) # Vẽ theo sns
    plt.legend() 
    plt.xlabel(x) # Label dữ liệu trục x
    plt.ylabel(y) # Label dữ liệu trục y
    return plt.show()



def violin_strip(x, y, z, data, filters, title1, title2, Width=12, Height=6, hue="day", dodge=True, palette="Set2"):
    filters_ = data[data[z] == filters]
    plt.figure(figsize=(Width, Height))
    plt.subplot(2, 2, 1) # Mức độ hình
    plt.title(title1) # Title dữ liệu
    sns.violinplot(
            x= x,
            y= y,
            data=filters_,
        )
    hue_order = [
            "Sunday",
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
        ]
    plt.subplot(2, 2, 2)
    plt.title(title2)
    sns.stripplot(
            x= x,
            y= y,
            data=filters_,
            hue= hue,
            dodge=dodge,
            palette= palette,
            hue_order=hue_order,
        )
    return plt.show()




def bar_plot(groupby1, y, data, title1, title2, Width=12, Height=6, ascending=False):
    dff = (
        data.groupby(groupby1)[y]
        .sum()
        .sort_values(ascending=ascending)
        .reset_index()
        .head(15)
    )
    plt.figure(figsize=(Width, Height))
    plt.subplot(2, 2, 1) # Mức độ hình
    plt.title(title1) # Title dữ liệu
    sns.barplot(
            x=groupby1, 
            y=y, 
            data=data
        )
    plt.subplot(2, 2, 2)
    plt.title(title2)
    sns.barplot(
            y=groupby1,
            x=y,
            data=data,
        )
    return plt.show()


def line_plot(groupby1, y, df, title, Width=12, Height=6, color="r"):
    data = (
        df.groupby(groupby1)[
            y
        ]
        .sum()
        .reset_index()
    )
    data[groupby1] = pd.to_datetime(data[groupby1])
    plt.figure(figsize=(Width, Height))
    plt.title(title)
    sns.lineplot(
        x=groupby1,
        y=y,
        data=data,
        color=color,
    )
    return plt.show()

def subplots(groupby1, y, z, v, df, title1, title2, top=15, Width=15, Height=6, ascending=False):
    dff = (
        df.groupby(groupby1)[y]
        .sum()
        .sort_values(ascending=ascending)
        .reset_index()
        .head(top)
    )
    plt.figure(figsize=(Width, Height))
    plt.title(title1) # Title dữ liệu
    sns.barplot(
        x=groupby1, y=y, data=dff
    )
    count_plot(x=z, y=v, data=df, title= title2, Width=15, Height=6)
    return plt.show()



def figure_axes(groupby1, y, z, v, df, title1, title2, top=15, Width=15, Height=6, ascending=False):
    dff = (
        df.groupby(groupby1)[y]
        .sum()
        .sort_values(ascending=ascending)
        .reset_index()
        .head(top)
    )
    plt.figure(figsize=(Width, Height))
    plt.subplot(1, 2, 1) # Mức độ hình
    plt.title(title1) # Title dữ liệu
    sns.barplot(
        x=groupby1,
        y=y,
        data=dff,
    )
    plt.subplot(1, 2, 2) # Mức độ hình
    plt.title(title2) # Title dữ liệu
    sns.countplot(x=z, hue=v, data=df)
    return plt.show()


def worldcloud(x, df, Width=2400, Height=2000, Width1 =12, Height1=15, background_color="white", off ="off"):
    corpus = " ".join(df[x].astype(str))
    wordcloud = WordCloud(
        stopwords=STOPWORDS, width=Width, background_color=background_color, height=Height
    ).generate(corpus)

    plt.figure(figsize=(Width1, Height1))
    plt.imshow(wordcloud)
    plt.axis(off)
    return plt.show()

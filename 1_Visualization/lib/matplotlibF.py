import matplotlib.pyplot as plt
import pandas as pd


Ghi_chu = """"
    1. Tại sao phải trực quan hóa dữ liệu
    2. Ưu điểm
        - Trực quan và dễ hiểu
        - Giải quyết vấn đề
        - Kể câu chuyện về dữ liệu trong thời gian ngắn nhất
    3. Nguyên tắc thiết kế
    3.1 Trustworthy
        - Sự tin tưởng khó kiếm, dễ mất
        - Tính trung thực và toàn vẹn cần phải có ở mọi nơi trong quá trình thực hiện data science
    3.2 Accessible
        - Ai là người xem biểu đồ
        - Hiểu được mục đích và trực quan hóa dữ liệu
    3.3 Elegant
        - Tập trung vào yếu tố liên quan
        - Có phong cách riêng nếu có thể
        - Suy nghĩ cách thiết kế trước khi thể hiện
    4. Matplotlib
        - Thư viện 2D của python
    5. Lý do dùng matplotlib
        - Cố găng mọi thứ dễ dàng hơn và những thứ khó khăn trở nên khả thi
        - Chỉ 1 số dòng code có thể sử dụng được
    6. Các loại biểu đồ
        - Bar (Cột), line, scatter (phân tán), histogram (Biểu đồ phân loại distribution và độ lệch chuẩn của dữ liệu), pie
        - Dữ liệu các trục (Axes data ranges)
        - Nhãn trên trục (Axes labels)
        - Ghi chú (legend)
        - Các chú thích (Annotation)
        - Figure là không gian thể hiện, cho phép nó trên đó có nhiều biểu đồ
        - Axes là biểu đồ thật sự với các thông tin: trục x-y, ghi chú, marker...
    7. Thành phần biểu đồ
        - plt.show() => Hiễn thị biểu đồ
        - plt.figure; plt.axes => Tạo figure, axis
        - plt.savefig(<Tên tập tin>) => Lưu biểu đồ
        - plt.title() => Tạo tiêu đề cho biểu đồ
        - plt.xlable(); plt.ylable() => Tạo tiêu đề cho trục x, y
        - plt.legend(loc=[<x>, <y>]) => Điều chỉnh vị trí ghi chú
        - plt.xticks(rotation=<degree>) => Thay đổi giá trị đơn vị trục x
        - plt.yticks(rotation=<degree>) => Thay đổi giá trị đơn vị trục y
        - plt.xlim(<min_value>, <max_value>) => Giới hạn trục x
        - plt.ylim(<min_value>, <max_value>) => Giới hạn trục y
        - plt.axis("off") => Tắt hiện thị trục x, y
        - plt.subplot(<nums>, <col>, <row>)
        - plt.imshow(<image>)
    8. Word clouds: con được gọi là text clouds và tag clouds
        - Càng nhiều tư đơn giản xuất hiện trong văn bản thì nó càng lớn và trọng tâm
        - Thể hiện sao được tâm quan trọng của mỗi từ thể hiện quá word clouds
        - Có thể loại bỏ 1 số từ không quan trọng file có 1 list

"""
# Hàm

# Load file dữ liệu
def load_data(file_path):
    df = pd.read_csv(file_path)
    return df


# Biểu đồ bar: là biểu đồ hình cột, nằm dọc
# Mục địch dữ liệu: Dùng để phân chia distribution hoặc nó là categories
def bar_chart(x, y, title, data, width=12, height=10, nHead=20, rotation = 80, style="plain", ascending=False):
    plt.figure(figsize=(width, height)) # Thay đổi kích thước biểu đồ
    plt.xticks(rotation=rotation) # Thay đổi giá trị trục x
    bar_data = data.sort_values(by=y, ascending=ascending) # Sắp sếp lại dữ liệu cao đến thấp
    bar_data = bar_data.head(nHead)
    plt.ticklabel_format(style=style) 
    chart = plt.bar(bar_data[x], bar_data[y]) # dữ liệu trục x và trục y
    plt.legend()
    plt.xlabel(x) # Label dữ liệu trục x
    plt.ylabel(y) # Label dữ liệu trục y
    plt.title(title) # Tạo tiều đề cho biểu đồ
    plt.show()
    return chart


# Biểu đồ bar: là biểu đồ hình cột, nằm ngang
# Mục địch dữ liệu: Dùng để phân chia distribution hoặc nó là categories
def horizontal_chart(x, y, title, data, width=12, height=10, nHead=20, rotation = 80, style="plain", ascending=False):
    plt.figure(figsize=(width, height))  # Thay đổi kích thước biểu đồ
    plt.xticks(rotation=rotation) # Thay đổi giá trị trục x
    bar_data = data.sort_values(by=y, ascending=ascending) # Sắp sếp lại dữ liệu cao đến thấp
    bar_data = bar_data.head(nHead)
    plt.ticklabel_format(style=style)
    chart = plt.barh(bar_data[x], bar_data[y]) # dữ liệu trục x và trục y
    plt.legend()
    plt.xlabel(x) # Label dữ liệu trục x
    plt.ylabel(y) # Label dữ liệu trục y
    plt.title(title)  # Tạo tiều đề cho biểu đồ
    plt.show()
    return chart

# Biểu đồ là biểu đồ phân tán dữ liệu y so với x xem mức độ tương tác dữ liệu
# Mục đích: Là biểu đồ phân loại distribution hoặc relationships dữ liệu 2 biến, 3 biến
def visualize_scatter(x, y, z, title, data, width=12, height=10, marker="*", alpha=0.5):
    plt.figure(figsize=(width, height)) # Thay đổi kích thước biểu đồ
    chart = plt.scatter(
        x=data[x], # Dữ liệu trục x
        y=data[y], # Dữ liệu trục y
        marker=marker, # Kiểu hiện thị đường kẻ
        s=data[z],
        c=data[z],
        alpha=alpha # Độ công của dữ liệu
        )
    plt.legend()
    plt.xlabel(x) # Label dữ liệu trục x
    plt.ylabel(y) # Label dữ liệu trục y
    plt.title(title)  # Tạo tiều đề cho biểu đồ
    plt.show()
    return chart

# Biểu đồ histogram mục đích dùng để xem mực độ tập trung dữ liệu hay mực độ phân phối dữ liệu
# Mục đích: Xem dữ liệu độ lệch chuẩn thể nào và có tập trung không 
def histogram(x, title, data, width=12, height=10, color="y", bins = 50):
    plt.figure(figsize=(width, height)) # Thay đổi kích thước biểu đồ
    chart = plt.hist(data[x], color=color, bins=bins) # Dữ liệu trục x, màu sắc, mực độ dữ liệu tập trung
    plt.xlabel(x) # Label dữ liệu trục x
    plt.legend()
    plt.title(title)  # Tạo tiều đề cho biểu đồ
    plt.show()
    return chart

# Biểu đồ hình tròn mục đích chủ yếu dùng để thực hiện tỉ trọng của các thành phần chính
# Mục đích: Dùng để phân tích static thống kê dữ liệu
def pie_chart(groups, x, title, data, width=12, height=10, ascending=False, explode = (0.1, 0, 0, 0, 0, 0, 0), shadow=True):
    days_data = (
        data.groupby(groups)[x] # Groupby dữ liệu
        .sum() # Sum theo ngày chú ý dữ liệu phải type float
        .sort_values(ascending=ascending) # Sort dữ liệu
        .reset_index() # Reset lại index để dữ liệu đúng với index theo tứ tự
    )
    plt.figure(figsize=(width, height)) # Kích thước của dữ liệu
    chart = plt.pie(
        days_data[x], # Dữ liệu x
        labels=days_data[groups], # Groupby dữ liệu
        shadow=shadow, 
        explode=explode,
        autopct="%1.1f%%",
    ) # Dữ liệu trục x, group theo tiêu chí và tỉ lệ %
    plt.xlabel(x) # Label dữ liệu trục x
    plt.title(title)  # Tạo tiều đề cho biểu đồ
    plt.legend()
    plt.show()
    return chart

# Biểu đồ dùng để thực hiện nhiều biểu đồ cùng 1 lượt
# Mục đích: 2 loại biểu đồ visualize_scatter và  horizontal_chart
def two_subplots(x, y, z, v, title, data, width=12, height=10, nHead=20, ascending=False,  marker="*"):
    plt.figure(figsize=(width, height)) # Kích thước dữ liệu
    plt.subplot(1, 2, 1) # Vẽ nhiều biểu đồ
    bar_data = data.sort_values(by=y, ascending=ascending) # Sắp sếp dữ liệu
    bar_data = bar_data.head(nHead) # Chiều dài hiện thị số lượng dữ liệu
    chart1 = plt.barh(bar_data[v], bar_data[y]) # Biểu đồ bar
    plt.subplot(1, 2, 2) # Vẽ nhiều biểu đồ
    chart2 = plt.scatter(data[y], data[x], c=data[z], marker=marker)
    plt.title(title)  # Tạo tiều đề cho biểu đồ
    plt.legend()
    plt.show()
    return chart1 | chart2


# 4 loại biểu đồ hình tròn và biểu đồ hình bar_chart và biểu đồ hình line
# Mục đích:
def four_subplots(Groupby1, Groupby2, Groupby3, x,y, title1, title2, data, width=12, height=10, nHead=20, ascending=False,  shadow=True, rotation=80):
    days_data = (
        data.groupby(Groupby1)[x] # Groupby dữ liệu
        .sum() # Tính tỏng
        .sort_values(ascending=ascending) # Sắp sếp dữ liệu
        .reset_index() # Reset lại index dữ liệu
    )
    months_data = (
        data.groupby(Groupby2)[x] # Groupby dữ liệu 2
        .sum() # Sum dữ liệu
        .sort_values(ascending=ascending) # Sắp sếp dữ liệu
        .reset_index() # Reset index
    )
    plt.figure(figsize=(width, height)) # Kích thước dữ liệu
    plt.subplot(2, 2, 1) # Mức độ hình
    plt.title(title1) # Title dữ liệu
    chart1 = plt.pie(
        days_data[x], # DỮ liệu x
        labels=days_data[Groupby1],  # Groupby dữ liệu
        shadow=shadow, 
        autopct="%1.1f%%",
    )
    plt.subplot(2, 2, 2)
    plt.title(title2)
    chart2 = plt.pie(
        months_data[x],
        labels=months_data[Groupby2],
        shadow=shadow,
        autopct="%1.1f%%",
    )
    plt.subplot(2, 2, 3)
    bar_data = data.sort_values(by=x, ascending=ascending)
    bar_data = bar_data.head(nHead)
    plt.xticks(rotation=rotation)
    chart3 = plt.bar(bar_data[y], bar_data[x])
    plt.subplot(2, 2, 4)
    views = data.groupby(Groupby3)[x].sum().reset_index()
    chart4 = plt.plot(views[Groupby3], views[x])
    plt.show()
    return chart1 | chart2 | chart3 | chart4
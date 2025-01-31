import fastapi.middleware.cors
app = fastapi. FastAPI()
app.add_middleware(
fastapi.middleware.cors.CORSMiddleware,
allow_origins=["*"], # อนุญาตให้ทุกที่มา (ทุก domain) เข้าถึง API ได้
allow_credentials=True,
allow_methods=["*"], # อนุญาตให้ทุก HTTP method (GET, POST, DELETE ฯลฯ)
allow_headers=["*"], # อนุญาตให้ทุก headers

<script>
                   async function select_table(event) {
        event.preventDefault();
        const table = document.getElementById("table").value; 
        const apiurl = http://localhost:8000/select/shop_db/${table};
        const response = await fetch(apiurl);
        const data = await response.json();
        let table_data = "<table border='1'> <tr>";
        Object.keys(data.select_data[0]).forEach(key => {
        table_data += <th>${key}</th>;

        table_data += "</tr>";
        data.select_data.forEach(row => {
        table_data += "<tr>";
        Object.values(row).forEach(value => {
        table_data += <td>${value}</td>; 

        table_data += "</tr>";

        table_data += "</table>";
        / / แสดงตารางใน <div id="tableData">
        document.getElementById("tableData").innerHTML = table_data;
        </script>

<body>
<h3>แสดงข้อมูลในตาราง</h3>
<form onsubmit="select_table(event)">
mso <input type="text" id="table" name="table">
<button type="submit">ดูข้อมูล</button>
</form>
<div id="tableData">แสดงข้อมูลในตาราง</div>
</body>
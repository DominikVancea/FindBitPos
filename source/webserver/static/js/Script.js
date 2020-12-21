function SendData(data) {
    var Conn = new WebSocket('ws://localhost:5001')
    Conn.onmessage = function(e){ WriteData(e.data) }
    Conn.onopen = () => Conn.send(data)
};

function WriteData(data) {
    RecvData = JSON.parse(data)

    if (RecvData["Error"] != "") {
        document.getElementById("Recv").innerHTML = RecvData["Error"]
    }
    else {
        var BitTotalPos = 0
        BitTotalPos = parseInt(RecvData["BitPos"]) + (parseInt(RecvData["BytePos"]) * 8) - 8
        document.getElementById("Recv").innerHTML = "Bit Position: " + RecvData["BitPos"] + "<br>" + "Byte Position: " + RecvData["BytePos"] + "<br>"  + "Total Bit Position: " + BitTotalPos;
    }
};

//Read selected file and send call function SendData to send data to the websocket
const Input = document.querySelector("#Input");

Input.addEventListener("change", () => {
    const File = Input.files.item(0)

    const Reader = new FileReader()
    Reader.readAsText(File)
    Reader.onload = () => {
        SendData(Reader.result)
    }
})

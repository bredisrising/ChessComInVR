using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.Net;
using System.Net.Sockets;
using System.Text;
using System.Threading;


public class ChessTest : MonoBehaviour
{

    Thread mThread;
    public string connectionIP = "127.0.0.1";
    public int connectionPort = 25001;
    IPAddress localAdd;
    TcpListener listener;
    TcpClient client;
    

    bool running;

    // Start is called before the first frame update
    void Start()
    {
        ThreadStart ts = new ThreadStart(GetInfo);
        mThread = new Thread(ts);
        mThread.Start();
        Debug.Log("Started!");
    }

    void GetInfo()
    {
        localAdd = IPAddress.Parse(connectionIP);
        listener = new TcpListener(localAdd, connectionPort);
        listener.Start();

        client = listener.AcceptTcpClient();

        running = true;
        while (running)
        {
            SendAndRecieveData();
        }
        listener.Stop();
    }

    void SendAndRecieveData()
    {
        NetworkStream nwStream = client.GetStream();
        byte[] buffer = new byte[client.ReceiveBufferSize];

        //recieving Data from the host
        int bytesRead = nwStream.Read(buffer, 0, client.ReceiveBufferSize);
        string dataRecieved = Encoding.UTF8.GetString(buffer, 0, bytesRead);

        if(dataRecieved != null)
        {
            Debug.Log(dataRecieved);
            
            byte[] writeBuffer = Encoding.ASCII.GetBytes("Message Recieved!");
            
            nwStream.Write(writeBuffer, 0, writeBuffer.Length);
        }



    }
}

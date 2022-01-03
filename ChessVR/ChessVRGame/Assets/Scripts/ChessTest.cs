using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using System.Net;
using System.Net.Sockets;
using System.Text;
using System.Threading;
using Newtonsoft.Json;


public class ChessTest : MonoBehaviour
{
    Thread mThread;
    public string connectionIP = "127.0.0.1";
    public int connectionPort = 25001;
    IPAddress localAdd;
    TcpListener listener;
    TcpClient client;

    public bool hasReceived = false;
    bool running;

    public Dictionary<string, string> boardDict;
    public string jsonBoardDict;

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
            ReceiveData();
        }
        listener.Stop();
    }

    void ReceiveData()
    {
        NetworkStream nwStream = client.GetStream();
        byte[] buffer = new byte[client.ReceiveBufferSize];

        //receiving Data from the host
        int bytesRead = nwStream.Read(buffer, 0, client.ReceiveBufferSize);
        string dataReceived = Encoding.UTF8.GetString(buffer, 0, bytesRead);

        if (dataReceived != "" && hasReceived != true) hasReceived = true;

        if(dataReceived != null)
        {
            if (dataReceived[0] == '0')
            {

            }
            else if (dataReceived[0] == '1')
            {

            }
            else
            {
                //JsonConvert.DeserializeObject<>
                boardDict = JsonConvert.DeserializeObject<Dictionary<string, string>>(dataReceived);
            }


            Debug.Log(dataReceived);
            
            //byte[] writeBuffer = Encoding.ASCII.GetBytes("Message Recieved!");
            
            //nwStream.Write(writeBuffer, 0, writeBuffer.Length);
        }
    }

    private void OnApplicationQuit()
    {
        try
        {
            client.Close();

        }
        catch
        {
            Debug.Log("bruh");
        }

        try
        {
            listener.Stop();
        }
        catch
        {
            Debug.Log("2nd bruh");
        }

        try
        {
            mThread.Abort();
        }
        catch
        {
            Debug.Log("3rd bruh");
        }
    }
}

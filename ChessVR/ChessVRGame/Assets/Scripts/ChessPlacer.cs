using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class ChessPlacer : MonoBehaviour
{

    [SerializeField] ChessTest chessGrab;

    Dictionary<string, string> chessboard;
    // Start is called before the first frame update
    void Start()
    {
        chessboard = chessGrab.boardDict;
    }

    // Update is called once per frame
    void Update()
    {
        if (chessGrab.hasReceived && !chessGrab.boardDict.Equals(chessboard))
        {
            chessboard = chessGrab.boardDict;
             
            Debug.Log(chessGrab.boardDict.ToString());
        }
    }
}

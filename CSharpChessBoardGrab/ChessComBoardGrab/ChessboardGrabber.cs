using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;
using System;
using System.Net;
using System.Net.Sockets;


namespace ChessComBoardGrab
{
    class ChessboardGrabber
    {
        static void Main(string[] args)
        {
            IWebDriver browser;
            browser = new ChromeDriver();
            browser.Navigate().GoToUrl("https://chess.com/");
        }
    }
}

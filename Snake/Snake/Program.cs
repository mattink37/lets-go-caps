using System;

namespace Snake
{
  class GameLogic
  {
    public GameLogic()
    {
      while (true)
      {
        input();
        update();
      }
    }

    void update()
    {
      Console.Clear();
    }

    void input()
    {

    }
  }
  class Program
  {
    static void Main(string[] args)
    {
      GameLogic gameLogic = new GameLogic();
    }
  }
}

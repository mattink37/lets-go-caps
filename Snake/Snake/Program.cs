using System;
using System.Collections.Generic;

namespace Snake
{
  class GameLogic
  {
    private const char _Snake = 'O';
    private const char _Food = '*';
    private const char _Wall = '#';
    private int _GridSize = 0;
    private char[][] _Grid;
    public GameLogic(int gridSize)
    {
      _GridSize = gridSize;
      Generate();
      DrawGrid();
      while (true)
      {
        Input();
        Update();
      }
    }

    void Generate()
    {
      GenerateGrid();
      GenerateSnake();
      GenerateFood();
    }

    void GenerateGrid()
    {
      _Grid = new char[_GridSize][];
      for (int y = 0; y < _GridSize; y++)
      {
        _Grid[y] = new char[_GridSize];
        for (int x = 0; x < _GridSize; x++)
        {
          if (y == 0 || x == 0 || y == _GridSize - 1 || x == _GridSize - 1)
          {
            _Grid[y][x] = _Wall;
          }
        }
      }
    }

    void GenerateSnake()
    {

    }

    void GenerateFood()
    {

    }

    void DrawGrid()
    {
      for (int y = 0; y < _GridSize; y++)
      {
        for (int x = 0; x < _GridSize; x++)
        {
          Console.Write(_Grid[y][x] + " ");
        }
        Console.WriteLine();
      }
    }

    void Draw()
    {
    }

    void Update()
    {
      //Console.Clear();
      //if (Food is eaten)
      //{
      //  GenerateFood();
      //}
      Draw();
    }

    void Input()
    {

    }
  }
  class Program
  {
    static void Main(string[] args)
    {
      GameLogic gameLogic = new GameLogic(25);
    }
  }
}

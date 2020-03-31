using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BugTrackerClient
{
  /// <summary>
  /// Any Item that you see on an agile board. I.E. Stories, Categories, etc.
  /// </summary>
  class BoardItem
  {
    private int ID;
    private string title;

    public BoardItem(string title = "untitled")
    {
      this.ID = AssignStoryID();
      this.title = title;
    }

    public static void AssignStoryID()
    {
      //todo
      ID = 0;
    }
  }
}

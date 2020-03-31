using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BugTrackerClient
{
  class Story : BoardItem
  {
    private int ID = -1;
    private string title;
    private string description;
    private List<string> comments;
    private string activity;

    public Story(string title = "untitled", string description = "empty", string activity = "No Recent Activity")
    {
      this.title = title;
      this.description = description;
      this.comments = new List<string>();
      this.activity = activity;
    }

    public void UpdateTitle(string text)
    {

    }

    public void UpdateDescription(string text)
    {

    }

    public void AddComment(string text)
    {

    }
  }
}

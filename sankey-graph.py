import plotly.graph_objects as go
import urllib, json
import os 


if __name__ == '__main__':

  # url = 'https://raw.githubusercontent.com/plotly/plotly.js/master/test/image/mocks/sankey_energy.json'
  # response = urllib.request.urlopen(url)
  directory_of_dirv = os.path.dirname(os.path.realpath(__file__))
  json_file = f"{directory_of_dirv}/walk.json"
  with open(json_file) as f:
      data = json.loads(f.read())

      f.close()

  #print(data)


  # override gray link colors with 'source' colors
  opacity = 0.4
  # change 'magenta' to its 'rgba' value to add opacity
  # data['data'][0]['node']['color'] = ['rgba(255,0,255, 0.8)' if color == "magenta" else color for color in data['data'][0]['node']['color']]
  # data['data'][0]['link']['color'] = [data['data'][0]['node']['color'][src].replace("0.8", str(opacity))
  #                                     for src in data['data'][0]['link']['source']]

  fig = go.Figure(data=[go.Sankey(
      valueformat = ".0f",
      valuesuffix = "TWh",
      # Define nodes
      node = dict(
        pad = 15,
        thickness = 15,
        line = dict(color = "black", width = 0.5),
        label =  data['label'],
      #   color =  data['filetypes'][0].values()
      ),
      # Add links
      link = dict(
        source =  data['source'],
        target =  data['target'],
        value =  data['value'],
        label =  data['label'],
        color =  data['color']
      #   color =  data['data'][0]['link']['color']
  ))])

  fig.update_layout(title_text="Energy forecast for 2050<br>Source: Department of Energy & Climate Change, Tom Counsell via <a href='https://bost.ocks.org/mike/sankey/'>Mike Bostock</a>",
                    font_size=10)
  fig.show()
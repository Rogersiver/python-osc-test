import { useState } from 'react'
import reactLogo from './assets/react.svg'
import { SketchPicker } from 'react-color';
import axios from 'axios';
import './App.css'

type Color = {
  hex: string,
  rgb: {
      r: number,
      g: number,
      b: number,
      a: number,
    },
  hsl: {
      h: number,
      s: number,
      l: number,
      a: number,
    }
  }

function App() {
  const [color, setColor] = useState<Color>({
      hex: '000000',
      rgb: {
          r: 0,
          g: 0,
          b: 0,
          a: 1
        },
      hsl: {
          h: 0,
          s: 0,
          l: 0,
          a: 1,
        }
    })

  const handleChange = (color: Color) => {
      setColor(color);
    }

  const handleChangeComplete = async (color: Color) => {
     const response = await axios.post('http://localhost:5000/rgb', color);
      console.log(response.data);
    }
  return (
    <div className="App">
      <SketchPicker
        onChange={handleChange}
        color={color}
        onChangeComplete={handleChangeComplete}
      />
   </div>
  )
}

export default App

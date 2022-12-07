import { useState } from 'react'
import reactLogo from './assets/react.svg'
import { SketchPicker, Color } from 'react-color';
import axios from 'axios';
import './App.css'



function App()
{
  const [color, setColor] = useState<any>({
    rgb: {
      r: 0,
      g: 0,
      b: 0,
      a: 1
    }
  })

  const handleChange = async (color: any) =>
  {
    const response = await axios.post('http://192.168.1.160:5000/rgb', color);
    setColor(color.rgb);
  }

  const handleChangeComplete = async (color: any) =>
  {
    const response = await axios.post('http://192.168.1.160:5000/rgb', color);
    setColor(color.rgb);
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

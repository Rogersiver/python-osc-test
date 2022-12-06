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

  const handleChange = (color: any) =>
  {
    setColor(color.rgb);
  }

  const handleChangeComplete = async (color: any) =>
  {
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

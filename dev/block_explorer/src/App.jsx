import React, { useEffect, useState, useRef } from 'react'

function App() {

  const submitButtonRef = useRef(null);

  const [data, setData] = useState([])
  const [selectedOption, setSelectedOption] = useState('users');
  const [buttonClicked, setButtonClicked] = useState(false);
  const [inputValue, setInputValue] = useState('1');

  const handleOptionChange = (event) => {
    setSelectedOption(event.target.value);
  };

  const handleKeyPress = (event) => {
    if (event.key === 'Enter') {
      submitButtonRef.current.click();
    }
  };

  const handleInputChange = (event) => {
    setInputValue(event.target.value);
  };

  const handleButtonClick = () => {
    setButtonClicked(true);
  };

  useEffect(() => {
    fetch(`https://jsonplaceholder.typicode.com/${selectedOption}/${inputValue}`)
    .then(response => response.json())
    .then(json => setData(json))
    .then(setButtonClicked(false))
    }, [buttonClicked])


  return (
<div className="p-4">
      <h1>Explorer</h1>
      <div>
        <input onChange={handleInputChange} onKeyDown={handleKeyPress}></input>
        <button ref={submitButtonRef} onClick={handleButtonClick}>Filter</button>
      </div>

      <div>
        <form>
          <div>
            <label>
              <input type="radio" value="users" checked={selectedOption === 'users'} onChange={handleOptionChange} />
              users
            </label>
          </div>
          <div>
            <label>
              <input type="radio" value="posts" checked={selectedOption === 'posts'} onChange={handleOptionChange} />
              posts
            </label>
          </div>
          <div>
            <label>
              <input type="radio" value="comments" checked={selectedOption === 'comments'} onChange={handleOptionChange} />
              comments
            </label>
          </div>
        </form>
        <p>You selected: {selectedOption}</p>
      </div>

      <div className="mt-2">      
        { JSON.stringify(data) === '{}' ? <p>No Data available</p> : <p>{JSON.stringify(data)}</p> }
      </div>
    </div>

  )
}

export default App

import React, { useEffect, useState, useRef, useLayoutEffect } from 'react'
import Block from './Block'
import Transaction from './Transaction'
import Address from './Address'


function App() {

  const [data, setData] = useState({})
  const [rosourceType, setResourceType] = useState('search_block')
  const [inputValue, setInputValue] = useState('0');
  const [isLoading, setIsLoading] = useState(true);

  const handleInputChange = (event) => {
    if (event.target.value !== ''){
      setInputValue(event.target.value);
    } else {
      setInputValue('0')
    }
  };

    useLayoutEffect(() => {
      const fetchData = async () => {
        try {
          setIsLoading(true);
          const response = await fetch(`/${rosourceType}/${inputValue}`);
          const jsonData = await response.json();
          setData(jsonData);
          setIsLoading(false);
          console.log(import.meta.env.VITE_APP_ADDRESS);
        } catch (error) {
          console.error('Error fetching data:', error);
        }
      };
        fetchData();
    }, [rosourceType, inputValue]);

  return (

    <div className="container mx-auto my-32">
        <div>

            <div className="bg-white relative shadow rounded-lg w-5/6 md:w-5/6  lg:w-4/6 xl:w-3/6 mx-auto pb-3">
                <div className="flex justify-center">
                        <div className="rounded-md mx-auto absolute -top-20 w-32 h-32 shadow-md border-2 bg-gradient-to-tl from-indigo-700 to-sky-400 border-white transition duration-200 transform hover:scale-110"></div>
                </div>
                
                <div className="mt-16">
                    <h1 className="font-bold text-center text-3xl text-gray-900">Block Explorer</h1>
                    <p className="text-center text-sm text-gray-400 font-medium">Created by: Qusai Abudhaim</p>
                    <p>
                        <span>
                            
                        </span>
                    </p>
                    <div className="my-5 px-6">
                        <input onChange={handleInputChange} className="text-gray-500 w-full block rounded-lg text-center font-medium leading-6 px-6 py-3 border-2 border-gray-500"></input>
                    </div>
                    <div className="flex justify-between items-center my-5 px-6">
                        <button onClick={() => setResourceType('search_block')} className="text-gray-500 hover:text-gray-900 hover:bg-gray-100 rounded transition duration-100 ease-in font-medium text-lg text-center w-full py-3">Block</button>
                        <button onClick={() => setResourceType('search_transaction')} className="text-gray-500 hover:text-gray-900 hover:bg-gray-100 rounded transition duration-100 ease-in font-medium text-lg text-center w-full py-3">Transaction</button>
                        <button onClick={() => setResourceType('search_address')} className="text-gray-500 hover:text-gray-900 hover:bg-gray-100 rounded transition duration-100 ease-in font-medium text-lg text-center w-full py-3">Address</button>
                    </div>

                    <div className="w-full">

                        <div className="mt-1 w-full flex flex-col items-center overflow-hidden text-sm">
                            <div href="#" className="border-t border-gray-100 text-gray-600 py-4 pl-6 pr-3 w-full block">

                            { rosourceType === 'search_block' && !isLoading && <Block data={data}/> }
                            {rosourceType === 'search_transaction' && !isLoading && <Transaction data={data} />}
                            {rosourceType === 'search_address' && !isLoading && <Address data={data} />}

                            </div>
                        </div>

                    </div>
                </div>
            </div>

        </div>
    </div>

    )
}
{/* 
    <div classNameName="p-4 h-full w-full">
      <h1>Explorer</h1>
      <div>
        <input onChange={handleInputChange} onKeyDown={handleKeyPress}></input>
        <button ref={submitButtonRef} onClick={handleButtonClick}>Filter</button>
      </div>

      <div>
        <form>
          <div>
            <label>
              <input type="radio" value="block" checked={selectedOption === 'block'} onChange={handleOptionChange} />
              block
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

      <div classNameName="mt-2">      
        { JSON.stringify(data) === '{}' ? <p>No Data available</p> : <p>{JSON.stringify(data.pending_transactions)}</p> }
      </div>
    </div> */}



export default App

import React from 'react'

const Block = ({data}) => {

  if (!data.block) return <p className='font-bold'>Block not found</p>

  const info = JSON.stringify(data)
  const index = JSON.stringify(data.block.index)

  const timestamp = JSON.stringify(data.block.timestamp)
  const options = { year: 'numeric', month: 'long', day: 'numeric', hour: 'numeric', minute: 'numeric' };
  const date = new Date(timestamp * 1000).toLocaleString(undefined, options)

  const nonce = data.block.nonce
  const hash = data.block.hash
  const previousHash = data.block.previous_hash



  return (
    <div className='me-3'>
      
          <div className='flex justify-between items-center mb-3'>
            <p className='font-bold text-3xl'>Block #{index}</p>
            <p className='text-gray-500 hover:text-gray-900 transition duration-100 ease-in'>mined @{ date }</p>
          </div>
          
          <h1 className='font-bold text-2xl mt-4 mb-2'>Details</h1>
          <div className='flex justify-between items-center mb-2 border-b'>
            <p className='text-lg'>Nonce: </p>
            <p className='text-lg text-sky-600'>{ nonce }</p>
          </div>

          <div className='flex justify-between items-center mb-2 border-b'>
            <p className='text-lg'>Hash:</p>
            <p className='text-lg text-sky-600'>{ hash }</p>
          </div>

          <div className='flex justify-between items-center mb-2 border-b'>
            <p className='text-lg'>Previous hash:</p>
            <p className='text-lg text-sky-600'>{ previousHash }</p>
          </div>

          <h1 className='font-bold text-2xl mt-4 mb-2'>Transactions</h1>

          {data.block.transactions.map((transaction, index) => (
            (

              <div key={index} className='ms-5 mb-2'>
                <p><span className='font-bold text-lg'>Transaction  </span><span className='text-sky-600 font-bold'>#{transaction.transaction_id}</span></p>
                <p className='text-gray-500 ms-2'>@{new Date(transaction.timestamp * 1000).toLocaleString(undefined, options)}</p>
                <p className='ms-2'>Sender: {transaction.sender}</p>
                <p className='ms-2'>Recipient: {transaction.recipient}</p>
                <p className='ms-2'>Amount: {transaction.amount}</p>
              </div>

            )
          ))}

    </div>
  )
}

export default Block
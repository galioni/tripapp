import React from 'react';
import './App.css';

const options = {
  method: 'GET',
  headers: {
    'Accept': 'application/json',
    'Content-Type': 'application/json',
  },
  cors: true,
  credentials: 'same-origin'
};

class Country extends React.Component {
  state = {
    loading: true,
    countries: {}
  };
  
  async componentDidMount() {
    fetch("http://192.168.86.30:5000/country", options)
    .then(res => res.json())
    .then((countries) => {
      this.setState({ countries, loading: false })
    })
  }

  render() {
    if (this.state.loading) {
      return <div>loading...</div>;
    }

    if (!this.state.countries) {
      return <div>didn't get a country</div>;
    }

    return (
      <div>
        <label>Countries</label>
        <br />
        <select>
          {this.state.countries.map((country) => (
            <option value={country.id}>{country.name} - {country.code}</option>
          ))}
        </select>
      </div>
    );
  }
}

export default Country;
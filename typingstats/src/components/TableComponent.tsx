import { useState } from 'react';
import Table from 'react-bootstrap/Table';

interface Device {
  name: string;
  speed: number;
  accuracy: number;
}

const TableComponent = () => {
  const [devices, setDevices] = useState<Device[]>([
    { name: 'Mechanical Keyboard', speed: 280, accuracy: 99 },
    // Add more devices here
  ]);

  return (
    <div className="container">
      <h2>Your Typing Stats</h2>
      <Table striped bordered hover>
        <thead>
          <tr>
            <th>Device</th>
            <th>Speed</th>
            <th>Accuracy</th>
          </tr>
        </thead>
        <tbody>
          {devices.map((device, index) => (
            <tr key={index}>
              <td>{device.name}</td>
              <td>{device.speed} WPM</td>
              <td>{device.accuracy}%</td>
            </tr>
          ))}
        </tbody>
      </Table>
    </div>
  );
};

export default TableComponent;
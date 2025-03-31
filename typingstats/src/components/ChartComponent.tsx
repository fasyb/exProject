import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, ResponsiveContainer } from 'recharts';

interface DataPoint {
  date: string;
  speed: number;
  accuracy: number;
}

const ChartComponent = () => {
  const data: DataPoint[] = [
    { date: 'Jan 01', speed: 250, accuracy: 95 },
    { date: 'Jan 15', speed: 270, accuracy: 97 },
    { date: 'Feb 01', speed: 290, accuracy: 98 },
    // Add more data points here
  ];

  return (
    <ResponsiveContainer width="100%" height={300}>
      <LineChart data={data}>
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="date" />
        <YAxis />
        <Tooltip />
        <Line type="monotone" dataKey="speed" stroke="#8884d8" activeDot={{ r: 8 }} />
        <Line type="monotone" dataKey="accuracy" stroke="#82ca9d" />
      </LineChart>
    </ResponsiveContainer>
  );
};

export default ChartComponent;
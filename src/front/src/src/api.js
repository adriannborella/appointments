export function useApi() {
  const getAppointments = async () => {
    const response = await fetch('http://localhost:11000/api/v1/appointment/');
    const data = await response.json();
    data.events = data.results.map((item, index) => {
      return {
        start: new Date(item.date_start),
        end: new Date(item.date_until),
        title: item.state,
      };
    });
    return data;
  };
  return {
    getAppointments,
  };
}

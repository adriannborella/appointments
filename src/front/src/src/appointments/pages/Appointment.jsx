import {useQuery} from 'react-query';
import {useApi} from '../../api';
import {Calendar, dateFnsLocalizer} from 'react-big-calendar';

import 'react-big-calendar/lib/css/react-big-calendar.css';

import format from 'date-fns/format';
import parse from 'date-fns/parse';
import startOfWeek from 'date-fns/startOfWeek';
import getDay from 'date-fns/getDay';
import enUS from 'date-fns/locale/en-US';

const locales = {
  'en-US': enUS,
};

const localizer = dateFnsLocalizer({
  format,
  parse,
  startOfWeek,
  getDay,
  locales,
});

export default function AppointmentPage() {
  const {getAppointments} = useApi();
  const {isLoading, data, error, refetch} = useQuery(['appointment'], () =>
    getAppointments().then((res) => res),
  );

  if (isLoading) {
    return <div>Loading</div>;
  }

  if (error) return <div>'An error has occurred: ' + error.message;</div>;
  console.log(data);
  return (
    <div>
      AppointmentPage
      <hr />
      <span>Total appointments: {data.count}</span>
      <button onClick={refetch}>Refrescar</button>
      <hr />
      <Calendar
        localizer={localizer}
        events={data.events}
        startAccessor="start"
        endAccessor="end"
        style={{height: 500}}
      />
    </div>
  );
}

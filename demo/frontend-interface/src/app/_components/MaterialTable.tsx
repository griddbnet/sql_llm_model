import { useMemo } from 'react';
import {
  MaterialReactTable, //import alternative sub-component if we do not want toolbars
  type MRT_ColumnDef,
  useMaterialReactTable,
} from 'material-react-table';


type Col = {
  header: string,
  accessorKey: string,
}

type GenericRowData = {
  [key: string]: unknown;
}

export const MaterialTable = (
  props:
    {
      modelTime: number;
      queryTime: number;
      queryResults: string[][]
    }
) => {
  const { modelTime, queryTime, queryResults } = props

  const cols: Col[] = []

  for (let i = 0; i < queryResults[0].length; i++) {
    const tmp = {
      accessorKey: `col-#-${i}`,
      header: `col-#-${i}`,
      muiTableBodyCellProps: {
        align: "center"
      },
      muiTableHeadCellProps: {
        align: "center"
      }
    }
    cols.push(tmp)
  }

  const columns = useMemo<MRT_ColumnDef<GenericRowData>[]>(
    () => cols,
    [queryResults, cols],
  );

  const data = useMemo(() => {
    let n = queryResults.length
    const chartData: GenericRowData[] = new Array(n)
    queryResults.forEach((row, jidx) => {
      const tmp: GenericRowData = {}
      row.forEach((val, idx) => {
        const keyName: string = `col-#-${idx}`
        tmp[keyName] = val.toString()
      })
      chartData[jidx] = tmp;
    })
    return chartData
  }, [queryResults])

  const baseBackgroundColor = '#1F2041'


  const table = useMaterialReactTable({
    columns,
    data: data,
    enableKeyboardShortcuts: false,
    enableColumnActions: false,
    enableColumnFilters: false,
    enableTopToolbar: false,
    enablePagination: true,
    enableSorting: false,
    positionPagination: "both",
    muiPaginationProps: {
      color: 'secondary',
      shape: 'rounded',
      showRowsPerPage: true,
    },
    muiTableBodyRowProps: { hover: false },
    mrtTheme: () => ({
      baseBackgroundColor: baseBackgroundColor,
    }),
    muiTableProps: {
      sx: {
        border: '1px solid rgba(81, 81, 81, .5)',
        caption: {
          captionSide: 'top',
        },
        color: 'white',

      },
    },
    muiTableHeadCellProps: {
      sx: {
        border: '1px solid rgba(81, 81, 81, .5)',
        fontWeight: 'bold',
        color: 'white',
        backgroundColor: '#4B3F72',
      },
    },
    muiTableBodyCellProps: {
      sx: {
        border: '1px solid rgba(81, 81, 81, .5)',
        color: 'white',
      },
    },
    renderCaption: ({ table }) =>
      `Model Time: ${modelTime.toFixed(2)} seconds || Query Time: ${queryTime.toFixed(2)} seconds`,
  });


  return <MaterialReactTable table={table} />;
};

export default MaterialTable;

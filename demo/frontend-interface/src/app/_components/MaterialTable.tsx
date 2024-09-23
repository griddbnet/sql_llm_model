import { useMemo } from 'react';
import {
  MRT_Table, //import alternative sub-component if we do not want toolbars
  type MRT_ColumnDef,
  useMaterialReactTable,
} from 'material-react-table';

type Col = {
  header: string,
  accessorKey: string
}

type GenericRowData = {
  [key: string]: unknown;
}

export const MaterialTable = ({ queryResults }: { queryResults: string[][] }) => {

  const cols: Col[] = []

  for (let i = 0; i < queryResults[0].length; i++) {
    const tmp = {
      accessorKey: `col-#-${i}`,
      header: `col-#-${i}`,
    }
    cols.push(tmp)
  }

  const columns = useMemo<MRT_ColumnDef<any>[]>(
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

  const table = useMaterialReactTable({
    columns,
    data: data,
    enableKeyboardShortcuts: false,
    enableColumnActions: false,
    enableColumnFilters: false,
    enablePagination: false,
    enableSorting: false,
    mrtTheme: (theme) => ({
      baseBackgroundColor: theme.palette.background.default, //change default background color
    }),
    muiTableBodyRowProps: { hover: false },
    muiTableProps: {
      sx: {
        border: '1px solid rgba(81, 81, 81, .5)',
        caption: {
          captionSide: 'top',
        },
      },
    },
    muiTableHeadCellProps: {
      sx: {
        border: '1px solid rgba(81, 81, 81, .5)',
        fontStyle: 'italic',
        fontWeight: 'normal',
      },
    },
    muiTableBodyCellProps: {
      sx: {
        border: '1px solid rgba(81, 81, 81, .5)',
      },
    },
    renderCaption: ({ table }) =>
      `Here is a table rendered with the lighter weight MRT_Table sub-component, rendering ${table.getRowModel().rows.length} rows.`,
  });

  //using MRT_Table instead of MaterialReactTable if we do not need any of the toolbar components or features
  return <MRT_Table table={table} />;
};

export default MaterialTable;

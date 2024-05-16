extern int printf(const char *format, ...);

#define read_csr(reg) ({ unsigned long __tmp;    \
  asm volatile ("csrr %0, " #reg : "=r"(__tmp)); \
  __tmp; })

#define START_STATS()                                                   \
  volatile long unsigned cycles_cntr_start           = read_csr(cycle);   \
  volatile long unsigned instrs_cntr_start           = read_csr(instret); \
  volatile long unsigned icachemiss_start            = read_csr(0xC03);   \
  volatile long unsigned dcachemiss_start            = read_csr(0xC04);   \
  volatile long unsigned levent_start                = read_csr(0xC05);   \
  volatile long unsigned sevent_start                = read_csr(0xC06);   \
  volatile long unsigned ifempty_start               = read_csr(0xC07);   \
  volatile long unsigned stall_start                 = read_csr(0xC08);   \
  volatile long unsigned perf_ext_evt_00_start       = read_csr(0xC09);   \
  volatile long unsigned perf_ext_evt_01_start       = read_csr(0xC0A);   \
  volatile long unsigned perf_ext_evt_02_start       = read_csr(0xC0B);   \
  volatile long unsigned perf_ext_evt_03_start       = read_csr(0xC0C);   \
  volatile long unsigned perf_ext_evt_04_start       = read_csr(0xC0D);   \
  volatile long unsigned perf_ext_evt_05_start       = read_csr(0xC0E);   \
  volatile long unsigned perf_ext_evt_06_start       = read_csr(0xC0F);   \
  volatile long unsigned perf_ext_evt_07_start       = read_csr(0xC10);   \
  volatile long unsigned out_snoop_read_once_start      = read_csr(0xC12);   \
  volatile long unsigned out_snoop_read_shared_start    = read_csr(0xC13);   \
  volatile long unsigned out_snoop_read_unique_start    = read_csr(0xC14);   \
  volatile long unsigned out_snoop_read_no_snoop_start  = read_csr(0xC15);   \
  volatile long unsigned out_snoop_clean_unique_start   = read_csr(0xC16);   \
  volatile long unsigned out_snoop_wr_unique_start      = read_csr(0xC17);   \
  volatile long unsigned out_snoop_wr_nosnoop_start     = read_csr(0xC18);   \
  volatile long unsigned out_snoop_snoop_wrback_start   = read_csr(0xC19)

#define STOP_STATS() \
  volatile long unsigned cycles_cntr           =  read_csr(cycle)   - cycles_cntr_start;       \
  volatile long unsigned instrs_cntr           =  read_csr(instret) - instrs_cntr_start;     \
  volatile long unsigned icachemiss            =  read_csr(0xC03)   - icachemiss_start ; \
  volatile long unsigned dcachemiss            =  read_csr(0xC04)   - dcachemiss_start ; \
  volatile long unsigned levent                =  read_csr(0xC05)   - levent_start     ; \
  volatile long unsigned sevent                =  read_csr(0xC06)   - sevent_start     ; \
  volatile long unsigned ifempty               =  read_csr(0xC07)   - ifempty_start    ; \
  volatile long unsigned stall                 =  read_csr(0xC08)   - stall_start      ; \
  volatile long unsigned perf_ext_evt_00       = read_csr(0xC09) - perf_ext_evt_00_start;   \
  volatile long unsigned perf_ext_evt_01       = read_csr(0xC0A) - perf_ext_evt_01_start;   \
  volatile long unsigned perf_ext_evt_02       = read_csr(0xC0B) - perf_ext_evt_02_start;   \
  volatile long unsigned perf_ext_evt_03       = read_csr(0xC0C) - perf_ext_evt_03_start;   \
  volatile long unsigned perf_ext_evt_04       = read_csr(0xC0D) - perf_ext_evt_04_start;   \
  volatile long unsigned perf_ext_evt_05       = read_csr(0xC0E) - perf_ext_evt_05_start;   \
  volatile long unsigned perf_ext_evt_06       = read_csr(0xC0F) - perf_ext_evt_06_start;   \
  volatile long unsigned perf_ext_evt_07       = read_csr(0xC10) - perf_ext_evt_07_start;   \
  volatile long unsigned out_snoop_read_once      = read_csr(0xC12) - out_snoop_read_once_start    ;   \
  volatile long unsigned out_snoop_read_shared    = read_csr(0xC13) - out_snoop_read_shared_start  ;   \
  volatile long unsigned out_snoop_read_unique    = read_csr(0xC14) - out_snoop_read_unique_start  ;   \
  volatile long unsigned out_snoop_read_no_snoop  = read_csr(0xC15) - out_snoop_read_no_snoop_start;   \
  volatile long unsigned out_snoop_clean_unique   = read_csr(0xC16) - out_snoop_clean_unique_start ;   \
  volatile long unsigned out_snoop_wr_unique      = read_csr(0xC17) - out_snoop_wr_unique_start    ;   \
  volatile long unsigned out_snoop_wr_nosnoop     = read_csr(0xC18) - out_snoop_wr_nosnoop_start   ;   \
  volatile long unsigned out_snoop_snoop_wrback   = read_csr(0xC19) - out_snoop_snoop_wrback_start 

#define PRINT_STATS() \
printf("%lu, %lu, %lu, %lu, %lu, %lu,  ", cycles_cntr               , instrs_cntr              , icachemiss             , dcachemiss          , levent               , sevent                 ); \
printf("%lu, %lu, %lu, %lu, %lu, %lu,  ", ifempty                   , stall                    ,  perf_ext_evt_00       , perf_ext_evt_01     , perf_ext_evt_02      , perf_ext_evt_03        ); \
printf("%lu, %lu, %lu, %lu, %lu, %lu,  ", perf_ext_evt_04           , perf_ext_evt_05          , perf_ext_evt_06        , perf_ext_evt_07     , out_snoop_read_once  , out_snoop_read_shared  ); \
printf("%lu, %lu, %lu, %lu, %lu, %lu \n", out_snoop_read_unique     , out_snoop_read_no_snoop  , out_snoop_clean_unique , out_snoop_wr_unique , out_snoop_wr_nosnoop , out_snoop_snoop_wrback )
